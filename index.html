// Function to dynamically add 9 subjects with names
function addSubjects() {
    const subjectsDiv = document.getElementById('subjects');
    const subjectNames = [
        "Professional English - I",
        "Heritage of Tamils",
        "Matrices and Calculus",
        "Engineering Physics",
        "Engineering Chemistry",
        "Problem Solving and Python Programming",
        "Physics and Chemistry Laboratory",
        "Problem Solving and Python Programming Laboratory",
        "English Laboratory"
    ];

    for (let i = 1; i <= 9; i++) {
        const subject = document.createElement('div');
        subject.className = 'subject';
        subject.innerHTML = `
            <label for="grade${i}">${subjectNames[i - 1]}:</label>
            <select id="grade${i}" name="grade${i}">
                <option value="10">O</option>
                <option value="9">A+</option>
                <option value="8">A</option>
                <option value="7">B+</option>
                <option value="6">B</option>
                <option value="5">C</option>
            </select>
            <label for="credits${i}">Credits:</label>
            <input type="number" id="credits${i}" name="credits${i}" min="1" max="10" required>
        `;
        subjectsDiv.appendChild(subject);
    }
}

// Function to calculate GPA
function calculateGPA() {
    let totalCredits = 0;
    let totalGradePoints = 0;

    for (let i = 1; i <= 9; i++) {
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

// Add 9 subjects when the page loads
window.onload = addSubjects;
