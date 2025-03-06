let subjectCount = 1;

function addSubject() {
    subjectCount++;
    const subjectsDiv = document.getElementById('subjects');
    const newSubject = document.createElement('div');
    newSubject.className = 'subject';
    newSubject.innerHTML = `
        <label for="grade${subjectCount}">Grade:</label>
        <select id="grade${subjectCount}" name="grade${subjectCount}">
            <option value="10">O</option>
            <option value="9">A+</option>
            <option value="8">A</option>
            <option value="7">B+</option>
            <option value="6">B</option>
            <option value="5">C</option>
        </select>
        <label for="credits${subjectCount}">Credits:</label>
        <input type="number" id="credits${subjectCount}" name="credits${subjectCount}" min="1" max="10" required>
    `;
    subjectsDiv.appendChild(newSubject);
}

function calculateGPA() {
    let totalCredits = 0;
    let totalGradePoints = 0;

    for (let i = 1; i <= subjectCount; i++) {
        const grade = parseFloat(document.getElementById(`grade${i}`).value);
        const credits = parseFloat(document.getElementById(`credits${i}`).value);

        if (!isNaN(grade) && !isNaN(credits)) {
            totalGradePoints += grade * credits;
            totalCredits += credits;
        }
    }

    if (totalCredits === 0) {
        document.getElementById('result').innerText = 'Please enter valid data.';
        return;
    }

    const gpa = (totalGradePoints / totalCredits).toFixed(2);
    document.getElementById('result').innerText = `Your GPA is: ${gpa}`;
}
