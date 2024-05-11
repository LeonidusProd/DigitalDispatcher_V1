import {createStore} from "vuex";
import {requestsModuleOld} from "@/store/requestsModuleOld";
import {settingsModule} from "@/store/settingsModule";
import {mainModule} from "@/store/mainModule";

export default createStore({
    modules: {
        requests: requestsModuleOld,
        settings: settingsModule,
        main: mainModule
    }
})