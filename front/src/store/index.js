import {createStore} from "vuex";
import {requestsModule} from "@/store/requestsModule";
import {settingsModule} from "@/store/settingsModule";
import {mainModule} from "@/store/mainModule";

export default createStore({
    modules: {
        requests: requestsModule,
        settings: settingsModule,
        main: mainModule
    }
})