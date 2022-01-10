
odoo.define('modulo016.wizard_hello_button', function (require) {
   "use strict";

   var core = require('web.core');

   var ListController = require('web.ListController');

   ListController.include({

       renderButtons: function($node) {
           this._super.apply(this, arguments);
               if (this.$buttons) {
                   let wizard_button = this.$buttons.find('.wizard_hello_button');
                   wizard_button && wizard_button.click(this.proxy('wizard_button')) ;
               }
       },

       wizard_button: function () {
            this.do_action({
               type: "ir.actions.act_window",
               name: "wizard hello",
               res_model: "product.template.hello.wizard",
               views: [[false,'form']],
               target: 'new',
               view_mode : 'form',
               flags: {'form': {'action_buttons': true, 'options': {'mode': 'edit'}}}
               });
           return { 'type': 'ir.actions.client', 'tag': 'reload', }
       }

   });

})
