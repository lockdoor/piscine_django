from django.shortcuts import render
import math

# Create your views here.
def index(request):
	colors: list = []
	shade: list[str] = []
	step: int = 50
	for x in range(step):
		color = 255 - math.floor(255 / step * x)
		c_hex = hex(color)[2:]
		c_hex = '0' + c_hex if len(c_hex) == 1 else c_hex
		shade.append(c_hex)
	for x in shade:
		colors.append({
			'red': f'#{x}0000',
			'green': f'#00{x}00',
			'blue': f'#0000{x}',
			'black': f'#{x}{x}{x}'
		})

	return render(request, 'ex03/index.html', {'colors': colors})
