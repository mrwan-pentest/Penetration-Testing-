import os
import re

# المجلد الرئيسي (حيث يوجد السكريبت)
root_dir = os.getcwd()

# مجلد الصور
images_dir = os.path.join(root_dir, "Images")

# التأكد من وجود مجلد الصور
if not os.path.exists(images_dir):
    print("❌ مجلد Images غير موجود!")
    exit()

# قائمة بكل ملفات Markdown في المجلد الرئيسي
md_files = [f for f in os.listdir(root_dir) if f.endswith('.md')]

if not md_files:
    print("❌ لا يوجد ملفات .md في المجلد!")
    exit()

print(f"🔍 تم العثور على {len(md_files)} ملفات Markdown")

for md_file in md_files:
    file_path = os.path.join(root_dir, md_file)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # البحث عن صيغة ![[اسم الملف.امتداد]]
    # واستبدالها بـ ![اسم الملف](./Images/اسم الملف.امتداد)
    new_content = re.sub(
        r'!\[\[(.*?)\]\]',
        r'![\1](./Images/\1)',
        content
    )

    # حفظ التغييرات
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✅ تم تعديل: {md_file}")

print("🎉 انتهى! جميع الروابط تم تحديثها.")