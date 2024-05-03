import {createStore} from "vuex";
import {requestsModule} from "@/store/requestsModule";

export default createStore({
    modules: {
        requests: requestsModule
    }
})