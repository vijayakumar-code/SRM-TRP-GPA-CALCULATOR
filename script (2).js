// Theme Switcher
function setTheme(theme) {
  document.body.className = theme;
}

// Add Subject
function addSubject() {
  const gpaInputs = document.getElementById('gpa-inputs');
  const newSubject = document.createElement('div');
  newSubject.className = 'subject';
  newSubject.innerHTML = `
    <input type="text" placeholder="Subject Name" class="subject-name">
    <select class="grade">
      <option value="10">O</option>
      <option value="9">A+</option>
      <option value="8">A</option>
      <option value="7">B+</option>
      <option value="6">B</option>
      <option value="5">C</option>
    </select>
    <input type="number" placeholder="Credits" class="credits" min="1">
  `;
  gpaInputs.appendChild(newSubject);
}

// Calculate GPA
function calculateGPA() {
  const subjects = document.querySelectorAll('.subject');
  let totalGradePoints = 0;
  let totalCredits = 0;

  subjects.forEach(subject => {
    const grade = parseFloat(subject.querySelector('.grade').value);
    const credits = parseFloat(subject.querySelector('.credits').value);
    totalGradePoints += grade * credits;
    totalCredits += credits;
  });

  const gpa = (totalGradePoints / totalCredits).toFixed(2);
  document.getElementById('gpa-result').textContent = `Your GPA is: ${gpa}`;
}

// Calculate CGPA
function calculateCGPA() {
  const totalCredits = parseFloat(document.getElementById('total-credits').value);
  const totalGradePoints = parseFloat(document.getElementById('total-grade-points').value);

  if (totalCredits > 0) {
    const cgpa = (totalGradePoints / totalCredits).toFixed(2);
    document.getElementById('cgpa-result').textContent = `Your CGPA is: ${cgpa}`;
  } else {
    document.getElementById('cgpa-result').textContent = 'Please enter valid values.';
  }
}
