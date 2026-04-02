---
name: Data Export
description: >
  Export research data in structured formats for integration with external tools.
  JSON for APIs and dashboards, CSV for spreadsheets. All exports include metadata.
  Triggered by "export", "download data", "CSV", "JSON", "spreadsheet".
---

# Data Export

## Export Formats and Use Cases

### Comparison Matrices to CSV

Convert technology comparison research into spreadsheet format:

- **Rows**: Technologies being evaluated
- **Columns**: Evaluation criteria
- **Cells**: Numeric scores, text ratings, or yes/no indicators

Useful for sharing with stakeholders, further analysis in spreadsheet tools, version control in Git.

### Tech Radar to JSON

Export Tech Radar entries in ThoughtWorks radar format (https://www.thoughtworks.com/radar):

- Compatible with build-your-own-radar tool
- Includes: name, ring (Adopt/Trial/Assess/Hold), quadrant, description
- Enables visualization in standard radar format
- Supports batch import of multiple entries

### Trend Data to CSV

Time series data exported as structured CSV:

- **Columns**: Date, Technology, Metric, Value, Confidence
- **Rows**: One per observation
- Sortable and plottable for trend analysis
- Include source annotations for traceability

### Scorecard Metrics to JSON

Structured export of evaluation scorecards:

```
{
  "technology": "...",
  "criteria": [
    {
      "name": "Performance",
      "weight": 0.3,
      "score": 8.5,
      "justification": "..."
    }
  ],
  "overall_score": 7.8,
  "recommendation": "..."
}
```

Suitable for dashboards, API consumption, further processing.

## Metadata Included in All Exports

Every export includes:
- Export date and timestamp
- Data version number
- List of sources used
- Confidence levels per entry
- Methodology notes
- User attribution if applicable

Enables audit trails and reproducibility.

## Export Workflow

1. Claude generates data structure in Python
2. Validates data integrity:
   - No missing required values
   - Correct data types
   - Consistent formatting
   - Score ranges within defined limits
3. Writes to file (CSV, JSON, or custom format)
4. Provides download link with file metadata
5. Logs export operation for audit trail

## Validation Rules

Before export, validate:
- All required fields populated
- Numeric values in appropriate ranges
- Dates in ISO 8601 format
- References and relations are consistent
- Text encoding is UTF-8 compliant
- No circular dependencies in relations
- Confidence levels match data completeness

Halt export and report specific validation errors if checks fail.
