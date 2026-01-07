/** @odoo-module */

import {patch} from "@web/core/utils/patch";
import {registry} from "@web/core/registry";
import { session } from "@web/session";
const { DateTime } = luxon;

const ResConfigEdition = registry.category("view_widgets").get("res_config_edition");

patch(ResConfigEdition.prototype,'_res_config_patch',{
    setup(){
        this.serverVersion = session.server_version;
        this.expirationDate = session.expiration_date
            ? DateTime.fromSQL(session.expiration_date).toLocaleString(DateTime.DATE_FULL)
            : DateTime.now().plus({ days: 30 }).toLocaleString(DateTime.DATE_FULL);
    }
});