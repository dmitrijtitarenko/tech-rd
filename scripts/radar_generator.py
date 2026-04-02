#!/usr/bin/env python3
"""
Tech radar generator compatible with ThoughtWorks build-your-own-radar.

Takes technology entries with quadrant and ring assignments.
Outputs JSON compatible with ThoughtWorks radar tool and generates CSV summary.

Input: List of technologies with quadrant and ring assignments
Output: JSON data file and CSV summary
"""

import json
import csv
from datetime import datetime


def generate_radar_data(entries, filename='radar.json'):
    """
    Generate tech radar JSON and CSV files.

    Args:
        entries: List of dicts with keys: name, quadrant, ring, description,
                is_new (optional)
        filename: Output filename for JSON

    Returns:
        Dict with processed data
    """
    radar_entries = []

    for entry in entries:
        radar_entries.append({
            'name': entry['name'],
            'quadrant': entry['quadrant'],
            'ring': entry['ring'],
            'isNew': entry.get('is_new', False),
            'description': entry.get('description', '')
        })

    output = {
        'entries': radar_entries,
        'quadrants': ['Languages', 'Frameworks', 'Infrastructure', 'Data'],
        'rings': ['Adopt', 'Trial', 'Assess', 'Hold']
    }

    with open(filename, 'w') as f:
        json.dump(output, f, indent=2)

    csv_filename = filename.replace('.json', '.csv')
    csv_entries = [
        {'name': e['name'], 'quadrant': e['quadrant'], 'ring': e['ring'],
         'is_new': e['isNew'], 'description': e['description']}
        for e in radar_entries
    ]
    with open(csv_filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'quadrant', 'ring',
                                               'is_new', 'description'])
        writer.writeheader()
        writer.writerows(csv_entries)

    return {
        'json_file': filename,
        'csv_file': csv_filename,
        'entry_count': len(radar_entries),
        'entries': radar_entries
    }


if __name__ == "__main__":
    entries = [
        {
            'name': 'Rust',
            'quadrant': 'Languages',
            'ring': 'Trial',
            'description': 'Systems language with memory safety',
            'is_new': False
        },
        {
            'name': 'TypeScript',
            'quadrant': 'Languages',
            'ring': 'Adopt',
            'description': 'Typed superset of JavaScript',
            'is_new': False
        },
        {
            'name': 'React',
            'quadrant': 'Frameworks',
            'ring': 'Adopt',
            'description': 'JavaScript UI library',
            'is_new': False
        },
        {
            'name': 'Svelte',
            'quadrant': 'Frameworks',
            'ring': 'Assess',
            'description': 'Compiler-based UI framework',
            'is_new': True
        },
        {
            'name': 'Kubernetes',
            'quadrant': 'Infrastructure',
            'ring': 'Adopt',
            'description': 'Container orchestration platform',
            'is_new': False
        },
        {
            'name': 'PostgreSQL',
            'quadrant': 'Data',
            'ring': 'Adopt',
            'description': 'Relational database',
            'is_new': False
        },
        {
            'name': 'DuckDB',
            'quadrant': 'Data',
            'ring': 'Assess',
            'description': 'Embedded OLAP database',
            'is_new': True
        },
        {
            'name': 'Java',
            'quadrant': 'Languages',
            'ring': 'Hold',
            'description': 'Legacy but stable platform',
            'is_new': False
        }
    ]

    import os
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'examples')
    os.makedirs(output_dir, exist_ok=True)
    result = generate_radar_data(entries, os.path.join(output_dir, 'tech_radar.json'))

    print("Tech Radar Generator Output")
    print("="*60)
    print("JSON file: {}".format(result['json_file']))
    print("CSV file: {}".format(result['csv_file']))
    print("Total entries: {}".format(result['entry_count']))
    print("\nRadar Summary:")
    print("-"*60)
    for entry in result['entries']:
        new_marker = " [NEW]" if entry['isNew'] else ""
        print("{} - {} ({}){}".format(
            entry['name'],
            entry['quadrant'],
            entry['ring'],
            new_marker
        ))
