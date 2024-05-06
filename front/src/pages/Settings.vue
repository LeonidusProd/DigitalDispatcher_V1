<template>
  <div class="container">
    <div class="left-side-menu">
      <div class="up-block">
        <div class="logo-block">
          <img class="logo-img" src="@/assets/Лого%20текст%20снизу.svg" alt="logo">
        </div>
        <div class="menu-block">
          <my-button @click="this.activeSection = 'systemSettings'"
            :class="{'active-button':this.activeSection === 'systemSettings'}">
            Системные
          </my-button>
          <my-button @click="this.activeSection = 'organizationSettings'"
            :class="{'active-button':this.activeSection === 'organizationSettings'}">
            Организация
          </my-button>
          <my-button @click="this.activeSection = 'staffSettings'"
            :class="{'active-button':this.activeSection === 'staffSettings'}">
            Персонал
          </my-button>
          <my-button @click="this.activeSection = 'addressSettings'"
            :class="{'active-button':this.activeSection === 'addressSettings'}">
            Адреса
          </my-button>
          <!--          <my-button @click="changeSection('newRequests')"-->
          <!--                     :class="{'active-button':this.activeSection === 'newRequests'}">-->
          <!--            Новые заявки-->
          <!--          </my-button>-->
          <!--          <my-button @click="changeSection('activeRequests')"-->
          <!--                     :class="{'active-button':this.activeSection === 'activeRequests'}">-->
          <!--            Активные заявки-->
          <!--          </my-button>-->
        </div>
      </div>
      <div class="down-block">
        <my-button @click="">
          Выход
        </my-button>
      </div>
    </div>

    <div class="workspace">
      <SystemSettings v-if="this.activeSection === 'systemSettings'">
      </SystemSettings>

      <OrganizationSettings v-if="this.activeSection === 'organizationSettings'">
      </OrganizationSettings>

      <StaffSettings v-if="this.activeSection === 'staffSettings'">
      </StaffSettings>

      <AddressSettings v-if="this.activeSection === 'addressSettings'">
      </AddressSettings>
      <!--      <div class="requests-list">-->
      <!--        <requests-list-->
      <!--            :requests=this.requests-->
      <!--            :request-list-landing="requestListLanding">-->
      <!--        </requests-list>-->
      <!--      </div>-->

      <!--      <div class="request-card">-->
      <!--        <h4 v-if="this.activeRequestId === -1">Ни одна заявка не выбрана</h4>-->
      <!--        <RequestCard v-else :key="this.activeRequestId">-->
      <!--        </RequestCard>-->
      <!--      </div>-->
    </div>
  </div>
</template>

<script>
import RequestCard from "@/components/RequestManage/RequestCard.vue";
import RequestsList from "@/components/RequestManage/RequestsList.vue";
import MyButton from "@/components/UI/MyButton.vue";
import {defineComponent} from "vue";
import store from "@/store";
import {mapActions, mapGetters, mapMutations, mapState} from "vuex";
import ShortRequestCard from "@/components/RequestManage/ShortRequestCard.vue";
import SystemSettings from "@/components/Settings/SystemSettings.vue";
import AddressSettings from "@/components/Settings/AddressSettings.vue";
import StaffSettings from "@/components/Settings/StaffSettings.vue";
import OrganizationSettings from "@/components/Settings/OrganizationSettings.vue";

export default {
  components: {OrganizationSettings, StaffSettings, AddressSettings, SystemSettings, MyButton},
  // computed: {
  //   store() {
  //     return store
  //   },
  //   ...mapState({
  //     activeSection: state => state.settings.activeSettingsSection,
  //   }),
  //   ...mapGetters({})
  // },
  data() {
    return {
      activeSection: 'systemSettings',
    }
  },
  mounted() {

  },
  methods: {
    // ...mapMutations({
    //   setActiveSection: "settings/setActiveSettingsSection",
    // }),
    // ...mapActions({}),
  }
}
</script>

<style scoped>
.container {
  display: flex;
  justify-content: space-between;
  min-height: 400px;
  height: 94vh;
}

.left-side-menu {
  background-color: rgb(169, 168, 159, 0.2);
  width: 20%;
  padding: 10px;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.logo-block {
  text-align: center;
}

.logo-img {
  width: 50%;
}

.down-block {
  width: 100%;
}

.workspace {
  background-color: rgb(169, 168, 159, 0.2);
  width: 79%;
  padding: 20px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  border-radius: 20px;
}

.active-button {
  background-color: rgb(79, 212, 213);
}

.active-button:hover {
  background-color: rgb(79, 212, 213);
}
</style>