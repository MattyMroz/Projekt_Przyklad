![Obraz1](/img/code.png)
```HTML
<!DOCTYPE html>
<html lang="pl">

<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<style>
		.scrollup {
			width: 64px;
			height: 64px;
			text-decoration: none;
			background: url("img/up.png") no-repeat 0px 0px;
			position: fixed;
			right: 50px;
			bottom: 50px;
			display: none;
		}
	</style>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
	<script src="src/jquery.scrollTo.min.js"></script>

	<script>
		jQuery(function ($) {
			$.scrollTo(0);

			$('#link1').click(function () { $.scrollTo($('#part1'), 500); });
			$('#link2').click(function () { $.scrollTo($('#part2'), 500); });
			// itd. dla kolejnych linków
			$('.scrollup').click(function () { $.scrollTo($('body'), 1000); });
		});

		$(window).scroll(function () {
			if ($(this).scrollTop() > 300) $('.scrollup').fadeIn();
			else $('.scrollup').fadeOut();
		});
	</script>
	<title>ScrollTo</title>
</head>

<body>

	<a href="#" class="scrollup"></a>
	<ul>
		<li><a id="link1" href="#">Link 1</a></li>
		<li><a id="link2" href="#">Link 2</a></li>
	</ul>

	<h2 id="part1">Text1</h2>
	<!-- 30x <br> -->
	<h2 id="part2">Text2</h2>

</body>

</html>
```


```HTML
<!DOCTYPE html>
<html lang="pl">

<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<style>
		/* Styl dla przycisku przewijania */
		.scrollup {
			width: 64px;
			height: 64px;
			text-decoration: none;
			background: url("img/up.png") no-repeat 0px 0px;
			position: fixed;
			right: 50px;
			bottom: 50px;
			display: none;
		}
	</style>
	<!-- Link do jQuery  -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
	<!-- Połączenie z plikiem: https://github.com/flesler/jquery.scrollTo -->
	<script src="src/jquery.scrollTo.min.js"></script>
	<!-- Funkcje zarządzające scroll'owaniem -->
	<script>
		jQuery(function ($) {
			// Zresetuj scrolla
			$.scrollTo(0);

			// Jeśli klikniemy w link z menu, to scrollujemy do odpowiedniej sekcji o podanym id
			$('#link1').click(function () { $.scrollTo($('#part1'), 500); });
			$('#link2').click(function () { $.scrollTo($('#part2'), 500); });
			// itd. dla kolejnych linków

			// Jeśli klikniemy guzik to scrollujemy po początku body
			$('.scrollup').click(function () { $.scrollTo($('body'), 1000); });
		});

		// Pokaż podczas przewijania | Jeśli przwijamy > 300px to pokaż guzik
		$(window).scroll(function () {
			if ($(this).scrollTop() > 300) $('.scrollup').fadeIn();
			else $('.scrollup').fadeOut();
		});
	</script>
	<title>ScrollTo</title>
</head>

<body>

	<a href="#" class="scrollup"></a>
	<ul>
		<li><a id="link1" href="#">Link 1</a></li>
		<li><a id="link2" href="#">Link 2</a></li>
	</ul>

	<h2 id="part1">Text1</h2>
	<!-- 30x <br> -->
	<h2 id="part2">Text2</h2>

</body>

</html>
```