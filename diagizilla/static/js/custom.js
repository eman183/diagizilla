odoo.define('diagizilla.custom_js', function (require) {
    'use strict';

    var FormView = require('web.FormView');

    FormView.include({
        init: function () {
            this._super.apply(this, arguments);
            this.disableCreateButton();
        },

        disableCreateButton: function () {
            if (this.$buttons) {
                this.$buttons.find('.o_form_button_create').hide();
            }
        },
    });
});