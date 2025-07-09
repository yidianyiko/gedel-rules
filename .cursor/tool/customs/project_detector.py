#!/usr/bin/env python3
"""
Project Detection and Registration Tool
Automatically detects and registers projects
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import argparse

class ProjectDetector:
    def __init__(self, workspace_root: str = "."):
        self.workspace_root = Path(workspace_root).resolve()
        self.cursor_dir = self.workspace_root / ".cursor"
        self.projects_dir = self.cursor_dir / "projects"
        self.registry_file = self.projects_dir / "project_registry.json"
        self.templates_dir = self.projects_dir / "templates"
        
        self.projects_dir.mkdir(exist_ok=True)
        self.templates_dir.mkdir(exist_ok=True)
        
        self.registry = self._load_registry()
    
    def _load_registry(self) -> Dict:
        """Load project registry"""
        if self.registry_file.exists():
            with open(self.registry_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            return {
                "metadata": {
                    "version": "1.0.0",
                    "created": datetime.now().isoformat(),
                    "last_updated": datetime.now().isoformat(),
                    "total_projects": 0
                },
                "projects": {},
                "project_types": {
                    "nodejs": {
                        "indicators": ["package.json", "node_modules", "npm-shrinkwrap.json", "yarn.lock"],
                        "priority": 1
                    },
                    "python": {
                        "indicators": ["requirements.txt", "setup.py", "pyproject.toml", "Pipfile", "poetry.lock"],
                        "priority": 1
                    },
                    "java": {
                        "indicators": ["pom.xml", "build.gradle", "gradle.properties", "src/main/java"],
                        "priority": 1
                    },
                    "react": {
                        "indicators": ["package.json", "src/App.js", "src/App.tsx", "public/index.html"],
                        "priority": 2
                    },
                    "vue": {
                        "indicators": ["package.json", "vue.config.js", "src/main.js", "src/App.vue"],
                        "priority": 2
                    },
                    "fastapi": {
                        "indicators": ["main.py", "requirements.txt", "app/", "api/"],
                        "priority": 2
                    },
                    "django": {
                        "indicators": ["manage.py", "settings.py", "urls.py", "wsgi.py"],
                        "priority": 2
                    }
                },
                "active_project": None,
                "project_dependencies": {},
                "statistics": {
                    "total_knowledge_entries": 0,
                    "global_knowledge_entries": 0,
                    "project_knowledge_entries": 0
                }
            }
    
    def _save_registry(self):
        """Save project registry"""
        self.registry["metadata"]["last_updated"] = datetime.now().isoformat()
        with open(self.registry_file, 'w', encoding='utf-8') as f:
            json.dump(self.registry, f, indent=2, ensure_ascii=False)
    
    def detect_project_type(self, project_path: Path) -> Tuple[str, Dict]:
        """Detect project type"""
        project_types = self.registry["project_types"]
        detected_types = {}
        
        for project_type, config in project_types.items():
            score = 0
            found_indicators = []
            
            for indicator in config["indicators"]:
                if (project_path / indicator).exists():
                    score += 1
                    found_indicators.append(indicator)
            
            if score > 0:
                detected_types[project_type] = {
                    "score": score,
                    "indicators": found_indicators,
                    "priority": config["priority"]
                }
        
        if not detected_types:
            return "unknown", {}
        
        # 按优先级和分数排序
        sorted_types = sorted(
            detected_types.items(),
            key=lambda x: (x[1]["priority"], x[1]["score"]),
            reverse=True
        )
        
        return sorted_types[0][0], sorted_types[0][1]
    
    def extract_project_metadata(self, project_path: Path, project_type: str) -> Dict:
        """Extract project metadata"""
        metadata = {
            "name": project_path.name,
            "path": str(project_path.relative_to(self.workspace_root)),
            "type": project_type,
            "created": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat(),
            "status": "active"
        }
        
        # Extract specific information based on project type
        if project_type == "nodejs" or project_type == "react" or project_type == "vue":
            package_json = project_path / "package.json"
            if package_json.exists():
                try:
                    with open(package_json, 'r', encoding='utf-8') as f:
                        package_data = json.load(f)
                        metadata["version"] = package_data.get("version", "unknown")
                        metadata["description"] = package_data.get("description", "")
                        metadata["dependencies"] = {
                            "dependencies": list(package_data.get("dependencies", {}).keys()),
                            "devDependencies": list(package_data.get("devDependencies", {}).keys())
                        }
                except Exception as e:
                    print(f"Warning: Could not parse package.json: {e}")
        
        elif project_type == "python":
            requirements_txt = project_path / "requirements.txt"
            if requirements_txt.exists():
                try:
                    with open(requirements_txt, 'r', encoding='utf-8') as f:
                        dependencies = [line.strip().split('==')[0] for line in f if line.strip() and not line.startswith('#')]
                        metadata["dependencies"] = {"requirements": dependencies}
                except Exception as e:
                    print(f"Warning: Could not parse requirements.txt: {e}")
        
        return metadata
    
    def create_project_structure(self, project_name: str, project_type: str, metadata: Dict):
        """Create project knowledge management structure"""
        project_dir = self.projects_dir / project_name
        project_dir.mkdir(exist_ok=True)
        
        # Create project knowledge files
        files_to_create = [
            ("lessons.md", self.templates_dir / "lessons.md"),
            ("todo.md", self.templates_dir / "todo.md"),
            ("config.md", self.templates_dir / "config.md"),
            ("knowledge_index.json", self.templates_dir / "knowledge_index.json")
        ]
        
        for filename, template_path in files_to_create:
            if template_path.exists():
                target_file = project_dir / filename
                if not target_file.exists():
                    with open(template_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # 替换模板变量
                    content = content.replace("{PROJECT_NAME}", project_name)
                    content = content.replace("{PROJECT_TYPE}", project_type)
                    content = content.replace("{CREATED_DATE}", metadata["created"])
                    content = content.replace("{LAST_UPDATED}", metadata["last_updated"])
                    content = content.replace("{TECH_STACK}", project_type)
                    
                    with open(target_file, 'w', encoding='utf-8') as f:
                        f.write(content)
        
        # Update knowledge index
        knowledge_index_file = project_dir / "knowledge_index.json"
        if knowledge_index_file.exists():
            with open(knowledge_index_file, 'r', encoding='utf-8') as f:
                knowledge_index = json.load(f)
            
            knowledge_index["metadata"]["project_name"] = project_name
            knowledge_index["metadata"]["project_type"] = project_type
            knowledge_index["metadata"]["created"] = metadata["created"]
            knowledge_index["metadata"]["last_updated"] = metadata["last_updated"]
            
            with open(knowledge_index_file, 'w', encoding='utf-8') as f:
                json.dump(knowledge_index, f, indent=2, ensure_ascii=False)
    
    def scan_workspace(self) -> List[Dict]:
        """Scan workspace and detect all projects"""
        detected_projects = []
        
        # Scan all subdirectories in the workspace root
        for item in self.workspace_root.iterdir():
            if item.is_dir() and not item.name.startswith('.') and item.name != '.cursor':
                project_type, type_info = self.detect_project_type(item)
                
                if project_type != "unknown":
                    metadata = self.extract_project_metadata(item, project_type)
                    detected_projects.append({
                        "path": item,
                        "type": project_type,
                        "metadata": metadata,
                        "type_info": type_info
                    })
        
        return detected_projects
    
    def register_project(self, project_info: Dict) -> bool:
        """Register project to registry"""
        project_name = project_info["metadata"]["name"]
        
        if project_name in self.registry["projects"]:
            print(f"Project '{project_name}' already registered")
            return False
        
        # Add to registry
        self.registry["projects"][project_name] = project_info["metadata"]
        self.registry["metadata"]["total_projects"] += 1
        
        # Create project structure
        self.create_project_structure(
            project_name,
            project_info["type"],
            project_info["metadata"]
        )
        
        # Save registry
        self._save_registry()
        
        print(f"Successfully registered project: {project_name} ({project_info['type']})")
        return True
    
    def auto_discover_and_register(self) -> int:
        """Automatically discover and register all projects"""
        print("Scanning workspace for projects...")
        detected_projects = self.scan_workspace()
        
        if not detected_projects:
            print("No projects detected in workspace")
            return 0
        
        print(f"Found {len(detected_projects)} projects:")
        for project in detected_projects:
            print(f"  - {project['metadata']['name']} ({project['type']})")
        
        registered_count = 0
        for project in detected_projects:
            if self.register_project(project):
                registered_count += 1
        
        print(f"Successfully registered {registered_count} new projects")
        return registered_count
    
    def list_projects(self):
        """List all registered projects"""
        if not self.registry["projects"]:
            print("No projects registered")
            return
        
        print("Registered projects:")
        for name, metadata in self.registry["projects"].items():
            status = metadata.get("status", "unknown")
            project_type = metadata.get("type", "unknown")
            print(f"  - {name} ({project_type}) - {status}")
    
    def set_active_project(self, project_name: str) -> bool:
        """Set active project"""
        if project_name not in self.registry["projects"]:
            print(f"Project '{project_name}' not found")
            return False
        
        self.registry["active_project"] = project_name
        self._save_registry()
        print(f"Set active project to: {project_name}")
        return True

def main():
    parser = argparse.ArgumentParser(description="Project Detection and Registration Tool")
    parser.add_argument("--scan", action="store_true", help="Scan and register all projects")
    parser.add_argument("--list", action="store_true", help="List all registered projects")
    parser.add_argument("--set-active", type=str, help="Set active project")
    parser.add_argument("--workspace", type=str, default=".", help="Workspace root directory")
    
    args = parser.parse_args()
    
    detector = ProjectDetector(args.workspace)
    
    if args.scan:
        detector.auto_discover_and_register()
    elif args.list:
        detector.list_projects()
    elif args.set_active:
        detector.set_active_project(args.set_active)
    else:
        # Default to scanning
        detector.auto_discover_and_register()

if __name__ == "__main__":
    main() 