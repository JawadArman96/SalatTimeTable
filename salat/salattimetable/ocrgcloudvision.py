import io
import json
from google.cloud import vision

# Path to Google Cloud service account key file
SERVICE_ACCOUNT_FILE = "C:/Users/jawad/Downloads/ocr-google/lofty-layout-452011-h4-6c595afc149d.json"

def ocr_with_google_vision(image_path):
    """Perform OCR with Google Cloud Vision API and extract word positions"""
    
    # Initialize Google Cloud Vision client
    client = vision.ImageAnnotatorClient.from_service_account_file(SERVICE_ACCOUNT_FILE)

    # Load image
    with io.open(image_path, "rb") as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    
    # Perform OCR (text detection)
    response = client.text_detection(image=image)
    annotations = response.text_annotations

    # Extract full detected text
    if annotations:
        extracted_text = annotations[0].description
    else:
        return {"error": "No text detected"}

    words_data = []
    for text in annotations[1:]:  # First item is full text, others are individual words
        words_data.append({
            "text": text.description,
            "vertices": [(v.x, v.y) for v in text.bounding_poly.vertices]  # Position data
        })
    
    return {
        "full_text": extracted_text,
        "words": words_data
    }

# Example usage
image_path = "C:/Users/jawad/Downloads/costco/costco2.jpg"
result = ocr_with_google_vision(image_path)

# Save results to JSON file
with open("ocr_result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

# Print extracted text and bounding box data
print("Full Extracted Text:\n", result["full_text"])
# print("\nExtracted Words with Positions:\n", result["words"])

