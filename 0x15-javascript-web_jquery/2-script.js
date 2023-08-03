<!DOCTYPE html>
<html>
<head>
  <!-- Add the jQuery library -->
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

  <!-- Your HTML content -->
  <div id="red_header">Click me to change the header color!</div>
  <header>This is the header element</header>

  <script>
    // Wait for the document to be ready before executing the script
    $(document).ready(function() {
      // Add a click event listener to the DIV#red_header element
      $('#red_header').on('click', function() {
        // Update the text color of the header element to red (#FF0000)
        $('header').css('color', '#FF0000');
      });
    });
  </script>
</body>
</html>
