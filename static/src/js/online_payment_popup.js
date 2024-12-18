/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { OnlinePaymentPopup } from "@pos_online_payment/app/utils/online_payment_popup/online_payment_popup";

patch(OnlinePaymentPopup.prototype, {
  onClickOpenPaymentPage(event) {
    // Retrieve the `data-qr-code` attribute from the button
    const qrCode = event.target.getAttribute('data-qr-code');
    
    if (qrCode) {
      // Extract the part of the URL to decode
      const toUrl = qrCode.split('/barcode/QR/')[1]; // Extract the encoded string
      
      // Decode the URL-encoded part
      const decodedUrl = decodeURIComponent(toUrl.split('?')[0]); // Trim off any additional query parameters
      
      // Open the decoded URL in a new tab
      window.open(decodedUrl, '_blank');
    } else {
      console.error("QR Code is missing!");
    }
  },
});