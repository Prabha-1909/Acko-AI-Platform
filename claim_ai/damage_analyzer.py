import json
from PIL import Image

import google.generativeai as genai

from rag_chatbot.config import GEMINI_API_KEY


def analyze_damage_image(image_path):

    try:
        genai.configure(
            api_key=GEMINI_API_KEY
        )

        model = genai.GenerativeModel(
            "gemini-2.0-flash"
        )

        image = Image.open(image_path)

        prompt = """
        Analyze this vehicle damage image for an insurance claim.

        Return only valid JSON:
        {
            "damage_type": "scratch/dent/crack/partial_loss/total_loss",
            "affected_parts": "bumper, door, windshield, headlight, mirror, body panel",
            "severity": "minor/moderate/major",
            "severity_score": 1 to 10
        }
        """

        response = model.generate_content(
            [
                prompt,
                image
            ]
        )

        text = response.text.strip()
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        result = json.loads(text)

        return {
            "damage_type": result.get("damage_type", "unknown"),
            "affected_parts": result.get("affected_parts", "unknown"),
            "severity": result.get("severity", "moderate"),
            "severity_score": int(result.get("severity_score", 5)),
            "vision_status": "success"
        }

    except Exception as e:

        return {
            "damage_type": "manual_review",
            "affected_parts": "unknown",
            "severity": "moderate",
            "severity_score": 5,
            "vision_status": str(e)
        }