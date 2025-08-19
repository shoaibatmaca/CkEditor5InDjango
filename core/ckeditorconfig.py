CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_5_CUSTOM_CSS='writer/css/ckeditor.css'
CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading", "|",
            "bold", "italic", "underline", "strikethrough", "|",
            "fontColor", "fontBackgroundColor", "|",
            "link", "blockQuote", "code", "insertTable", "imageUpload",
            "numberedList", "bulletedList", "|",
            "undo", "redo"
        ],
        "height": 500,
        "width": "100%",
        "fontColor": {
            "colors": [
                {"color": "#000000", "label": "Black"},
                {"color": "#F44336", "label": "Red"},
                {"color": "#2196F3", "label": "Blue"},
                {"color": "#4CAF50", "label": "Green"},
                {"color": "#FFEB3B", "label": "Yellow"},
                {"color": "#FF9800", "label": "Orange"},
                {"color": "#9C27B0", "label": "Purple"},
                {"color": "#00BCD4", "label": "Cyan"},
                {"color": "#795548", "label": "Brown"},
                {"color": "#607D8B", "label": "Gray"},
                {"color": "#FFFFFF", "label": "White"},
            ],
            "columns": 5,
        },
        "fontBackgroundColor": {
            "colors": [
                {"color": "#000000", "label": "Black"},
                {"color": "#F44336", "label": "Red"},
                {"color": "#2196F3", "label": "Blue"},
                {"color": "#4CAF50", "label": "Green"},
                {"color": "#FFEB3B", "label": "Yellow"},
                {"color": "#FF9800", "label": "Orange"},
                {"color": "#9C27B0", "label": "Purple"},
                {"color": "#00BCD4", "label": "Cyan"},
                {"color": "#795548", "label": "Brown"},
                {"color": "#607D8B", "label": "Gray"},
                {"color": "#FFFFFF", "label": "White"},
            ],
            "columns": 5,
        },
    },
    "extends": {
        "toolbar": [
            "heading", "|",
            "bold", "italic", "underline", "strikethrough", "|",
            "link", "blockQuote", "code", "insertTable", "imageUpload",
            "numberedList", "bulletedList", "|",
            "undo", "redo"
        ],
        "height": 500,
        "width": "100%",
    },
}
