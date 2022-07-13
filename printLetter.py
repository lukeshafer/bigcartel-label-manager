import pdfkit


def printLetter(data: list):
    html_sample = """
      <html>
        <style>
          /* css */
          @media print {
            .new-page {
              page-break-before: always;
            }
          }
          /* !css */
        </style>"""

    # loop through data list and add name to html_sample with f strings
    # get address and index from data
    for index, address in enumerate(data):
        try:
            html_sample += f"""
            <!-- html -->
              <div {"class='new-page'" if index > 0 else ""}>
                <img src="/home/pi/Documents/repos/bigcartel-label-manager/returnaddress.png" width=300/>
                <div style="text-align: center; font: 500 1.3rem'Open Sans'; margin-top: 80px;line-height: 0.75 ">
                  <p>{address["name"]}</p>
                  <p>{address['address1']}</p>
                  <p>{address['address2']}</p>
                  <p>{address['city']}, {address['state']} {address['zip']}</p>
                  <p>{address['country']}</p>
                </div>
              </div>
            <!-- !html -->
            """
        except KeyError:
            pass

    html_sample += "</html>"

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
