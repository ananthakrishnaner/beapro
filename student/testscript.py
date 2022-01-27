from student.models import StudentProfile
from chat.utils import find_or_create_private_chat

student_lists = StudentProfile.objects.all()

for s in student_lists:
	for student in s.connections.all()
	chat = find_or_create_private_chat(s.user,student)
	chat.is_active = True
	chat.save() 