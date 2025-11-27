import os

# 리네이밍 대상 폴더 경로
folder = r"원하는 파일 경로 지정"

# 대상 확장자
allowed_exts = [".jpg", ".jpeg", ".png", ".webp"]
# allowed_exts = [".dds"]

# 폴더 안 파일들을 정렬된 순서로 불러오기
files = sorted([f for f in os.listdir(folder) if os.path.splitext(f)[1].lower() in allowed_exts])

start_num = 1  # 시작 숫자 지정

# 리네이밍 실행
for i, filename in enumerate(files, start=start_num):
    ext = os.path.splitext(filename)[1].lower()
    new_name = f"{i:02d}{ext}"  # 예: 01_loading.jpg
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
    print(f"Renamed: {filename} -> {new_name}")
