from django.shortcuts import render
from django.http import Http404, HttpResponse
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap
# Create your views here.


def index(request):
    return render(request, "index.html")


# def download(request, picture):
def download(request):
    screen_dims = {'iPhone 7/iPhone6(s)': (750, 1334),
                   'iPhone 7+/iPhone6+(s)': (1080, 1920),
                   'Galaxy S7': (1440, 2560)}

    if request.method == "POST":
        if 'quote' in request.POST and len(request.POST['quote']) > 1:
            # Get attributes from form
            phone_type = request.POST['phone']
            quote = request.POST['quote']
            text_color = request.POST['text_color']
            bg_color = request.POST['background_color']
            # Import font file
            font_file = 'HaloHandletter.otf'
            # Create blank image
            quote_image = Image.new('RGB', screen_dims[phone_type], bg_color)
            # Create a draw object
            draw_obj = ImageDraw.Draw(quote_image)
            # Parse text into multiple lines
            parsed = textwrap.wrap(quote, width=20)
            text = "\n".join(parsed)
            # Instantiate variables for centering text
            font_size = 1
            font = ImageFont.truetype('/Users/Adhaar/Desktop/Projects/phoneQuotes/quotes/HaloHandletter.otf', size=font_size)
            image_fraction = 0.75
            dims = screen_dims[phone_type]

            # Determine appropriate font size
            while draw_obj.multiline_textsize(text, font, spacing=5)[0] <= dims[0] * image_fraction:
                if abs(dims[1] - draw_obj.multiline_textsize(text, font, spacing=5)[1]):
                    font_size += 1
                    font = ImageFont.truetype('/Users/Adhaar/Desktop/Projects/phoneQuotes/quotes/HaloHandletter.otf', size=font_size)

            # Correct font size
            font_size -= 1
            font = ImageFont.truetype('/Users/Adhaar/Desktop/Projects/phoneQuotes/quotes/HaloHandletter.otf', size=font_size)

            # Draw on picture
            text_width, text_height = draw_obj.multiline_textsize(text, font, spacing=5)
            draw_obj.multiline_text(((dims[0]-text_width)/2, (dims[1]-text_height)/2), text, font=font, fill=text_color, align='center', spacing=5)
            del draw_obj

            # Create directory to return
            picture = {'quote_image': quote_image, 'dimensions': dims}

            response = HttpResponse(content_type="image/png")
            quote_image.save(response, "PNG")
            return response
        else:
            raise Http404
    else:
        raise Http404















