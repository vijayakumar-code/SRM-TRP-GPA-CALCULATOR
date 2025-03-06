// Function to dynamically add subjects divided into Theory and Practicals
function addSubjects() {
    const subjectsDiv = document.getElementById('subjects');

    // Theory Subjects
    const theorySubjects = [
        { name: "Professional English - I", credits: 3 },
        { name: "Heritage of Tamils", credits: 1 },
        { name: "Matrices and Calculus", credits: 4 },
        { name: "Engineering Physics", credits: 3 },
        { name: "Engineering Chemistry", credits: 3 },
        { name: "Problem Solving and Python Programming", credits: 3 }
    ];

    // Practical Subjects
    const practicalSubjects = [
        { name: "Physics and Chemistry Laboratory", credits: 2 },
        { name: "Problem Solving and Python Programming Laboratory", credits: 2 },
        { name: "English Laboratory", credits: 1 }
    ];

    // Add Theory Subjects
    const theorySection = document.createElement('div');
    theorySection.innerHTML = `<h3>Theory</h3>`;
    subjectsDiv.appendChild(theorySection);

    theorySubjects.forEach((subject, index) => {
        const subjectDiv = document.createElement('div');
        subjectDiv.className = 'subject';
        subjectDiv.innerHTML = `
            <label for="grade${index + 1}">${subject.name}:</label>
            <select id="grade${index + 1}" name="grade${index + 1}">
                <option value="10">O</option>
                <option value="9">A+</option>
                <option value="8">A</option>
                <option value="7">B+</option>
                <option value="6">B</option>
                <option value="5">C</option>
            </select>
            <label for="credits${index + 1}">Credits:</label>
            <input type="number" id="credits${index + 1}" name="credits${index + 1}" value="${subject.credits}" readonly>
        `;
        subjectsDiv.appendChild(subjectDiv);
    });

    // Add Practical Subjects
    const practicalSection = document.createElement('div');
    practicalSection.innerHTML = `<h3>Practicals</h3>`;
    subjectsDiv.appendChild(practicalSection);

    practicalSubjects.forEach((subject, index) => {
        const subjectDiv = document.createElement('div');
        subjectDiv.className = 'subject';
        subjectDiv.innerHTML = `
            <label for="grade${index + 7}">${subject.name}:</label>
            <select id="grade${index + 7}" name="grade${index + 7}">
                <option value="10">O</option>
                <option value="9">A+</option>
                <option value="8">A</option>
                <option value="7">B+</option>
                <option value="6">B</option>
                <option value="5">C</option>
            </select>
            <label for="credits${index + 7}">Credits:</label>
            <input type="number" id="credits${index + 7}" name="credits${index + 7}" value="${subject.credits}" readonly>
        `;
        subjectsDiv.appendChild(subjectDiv);
    });
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

// Add subjects when the page loads
window.onload = addSubjects;
