# 이미지 크기 조정 업그레이드 버전
from PIL import Image
import os

# 설정
input_folder = r"원하는 파일이 있는 퐁더 지정"
output_folder = os.path.join(input_folder, "resized")
target_size = (2560, 1440)  # 원하는 최종 크기 (가로, 세로)

# 저장 폴더 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def is_landscape(size):
    width, height = size
    return width >= height

def is_target_landscape(size):
    width, height = size
    return width >= height

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".webp")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            with Image.open(input_path) as img:
                original_orientation = is_landscape(img.size)
                target_orientation = is_target_landscape(target_size)

                # 회전이 필요한 경우
                if original_orientation != target_orientation:
                    img = img.rotate(90, expand=True)

                resized_img = img.resize(target_size, Image.LANCZOS)
                resized_img.save(output_path)
                print(f"✅ 처리 완료: {filename}")
        except Exception as e:
            print(f"❌ 오류 발생: {filename} -> {e}")

print("\n🎉 모든 이미지 변환 완료!")
