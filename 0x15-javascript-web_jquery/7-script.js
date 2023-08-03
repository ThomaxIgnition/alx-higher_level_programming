<!DOCTYPE html>
<html>
<head>
  <!-- Add the jQuery library -->
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

  <!-- Your HTML content -->
  <div id="character">Character name will be displayed here</div>

  <script>
    // Wait for the document to be ready before executing the script
    $(document).ready(function() {
      // Fetch the character data from the URL
      $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        method: 'GET',
        success: function(data) {
          // Update the content of DIV#character with the character name
          $('#character').text(data.name);
        },
        error: function() {
          $('#character').text('Error fetching character name.');
        }
      });
    });
  </script>
</body>
</html>
