$(function () {
	$('btn_translate').click(function () {
		const code = $('#language_code').val();
		$get.JSON('https://www.fourtonfish.com/hellosalut/?lang=' + code, function (resp) {
			$('#hello').html(resp.hello);
		});
	});
});
