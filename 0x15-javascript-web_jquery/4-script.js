<!DOCTYPE html>
<html>
<head>
  <!-- Add the jQuery library -->
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <style>
    .red {
      color: red;
    }
    .green {
      color: green;
    }
  </style>
</head>
<body>

  <!-- Your HTML content -->
  <div id="toggle_header">Click me to toggle the header class!</div>
  <header class="red">This is the header element</header>

  <script>
    // Wait for the document to be ready before executing the script
    $(document).ready(function() {
      // Add a click event listener to the DIV#toggle_header element
      $('#toggle_header').on('click', function() {
        // Toggle the class of the header element
        $('header').toggleClass('red green');
      });
    });
  </script>
</body>
</html>
