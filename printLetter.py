import pdfkit


def printLetter(options):
    html_sample = f"""
    <!-- html -->
    <html>
      <img src="/home/pi/Documents/repos/bigcartel-label-manager/returnaddress.png" width=300/>
      <div style="text-align: center; font: 500 1.3rem'Open Sans'; margin-top: 80px;line-height: 0.75 ">
        <p>{options['name']}</p>
        <p>{options['address1']}</p>
        <p>{options['address2']}</p>
        <p>{options['city']}, {options['state']} {options['zip']}</p>
        <p>{options['country']}</p>
      </div>
    </html>
    <!-- !html -->
    """

    options = {
        'page-size': 'A6',
        'margin-top': '0in',
        'margin-right': '0in',
        'margin-bottom': '0in',
        'margin-left': '0in',
        'orientation': 'landscape',
        'enable-local-file-access': None,
    }

    result = pdfkit.from_string(
        html_sample, output_path="sample.pdf", options=options)

    return result
