import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from claim_ai.damage_analyzer import analyze_damage_image

image_path = "uploads/claims/test_damage.jpg"

result = analyze_damage_image(image_path)

print(result)