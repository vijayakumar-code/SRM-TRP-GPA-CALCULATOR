import http.server
import socketserver
import json
from urllib.parse import urlparse, parse_qs

PORT = 8000

# Data structure to store courses and grades
courses = []

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL and query parameters
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        # Serve different routes
        if parsed_url.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.serve_home_page()
        elif parsed_url.path == "/courses":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.serve_courses()
        elif parsed_url.path == "/add":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.serve_add_page()
        else:
            # Serve static files (e.g., CSS, JS)
            super().do_GET()

    def do_POST(self):
        # Handle POST requests (e.g., adding a course)
        if self.path == "/add":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length).decode("utf-8")
            post_params = parse_qs(post_data)

            # Extract course details
            course_name = post_params.get("course_name", [""])[0]
            credits = float(post_params.get("credits", ["0"])[0])
            grade = post_params.get("grade", [""])[0]

            # Add course to the data structure
            courses.append({
                "course_name": course_name,
                "credits": credits,
                "grade": grade
            })

            # Redirect to home page
            self.send_response(303)
            self.send_header("Location", "/")
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def serve_home_page(self):
        # Generate HTML for the home page
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>GPA Calculator</title>
        </head>
        <body>
            <h1>GPA Calculator</h1>
            <a href="/add">Add Course</a>
            <h2>Courses</h2>
            <ul>
        """
        for course in courses:
            html += f"<li>{course['course_name']} ({course['credits']} credits) - Grade: {course['grade']}</li>"
        html += """
            </ul>
            <h2>GPA: {gpa}</h2>
        </body>
        </html>
        """.format(gpa=self.calculate_gpa())
        self.wfile.write(html.encode("utf-8"))

    def serve_add_page(self):
        # Generate HTML for the add course page
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Add Course</title>
        </head>
        <body>
            <h1>Add Course</h1>
            <form action="/add" method="POST">
                <label for="course_name">Course Name:</label>
                <input type="text" id="course_name" name="course_name" required>
                <br>
                <label for="credits">Credits:</label>
                <input type="number" id="credits" name="credits" step="0.5" required>
                <br>
                <label for="grade">Grade:</label>
                <select id="grade" name="grade" required>
                    <option value="A+">A+</option>
                    <option value="A">A</option>
                    <option value="B+">B+</option>
                    <option value="B">B</option>
                    <option value="C+">C+</option>
                    <option value="C">C</option>
                    <option value="D">D</option>
                    <option value="F">F</option>
                </select>
                <br>
                <button type="submit">Add Course</button>
            </form>
            <a href="/">Back to Home</a>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

    def serve_courses(self):
        # Serve courses as JSON
        self.wfile.write(json.dumps(courses).encode("utf-8"))

    def calculate_gpa(self):
        # Calculate GPA using a 10-point grading system
        GRADE_POINTS = {
            "A+": 10.0,
            "A": 9.0,
            "B+": 8.0,
            "B": 7.0,
            "C+": 6.0,
            "C": 5.0,
            "D": 4.0,
            "F": 0.0
        }
        total_credits = sum(course["credits"] for course in courses)
        total_grade_points = sum(course["credits"] * GRADE_POINTS[course["grade"]] for course in courses)
        return round(total_grade_points / total_credits, 2) if total_credits > 0 else 0

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
