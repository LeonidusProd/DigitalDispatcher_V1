import {createStore} from "vuex";
import {requestsModule} from "@/store/requestsModule";
import {settingsModule} from "@/store/settingsModule";

export default createStore({
    modules: {
        requests: requestsModule,
        settings: settingsModule
    }
})