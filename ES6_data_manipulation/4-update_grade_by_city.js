export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((obj) => obj.location === city)
    .map((student) => {
      const grades = newGrades.filter((obj) => obj.studentId === student.id);
      if (grades.length === 0) {
        return { ...student, grade: 'N/A' };
      }
      return { ...student, grade: grades[0].grade };
    });
}
