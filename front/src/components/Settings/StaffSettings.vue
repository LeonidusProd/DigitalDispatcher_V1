<template>
  <div class="inside-container">
    <div class="left-side">
<!--      <div class="office-block">-->
<!--        <div>-->
<!--          <h3>Управляющие компании</h3>-->

<!--          <SettingsListView :key="this.officesListKey"-->
<!--                            :empty-header="'Список УК пуст'"-->
<!--                            :elements-list="this.officesList"-->
<!--                            :model-name="'office'"-->
<!--                            @deleteElement="loadOffices">-->
<!--          </SettingsListView>-->
<!--        </div>-->

<!--        <MyButton @click="this.showOfficeDialog = true">-->
<!--          Добавить УК-->
<!--        </MyButton>-->

<!--        <CreateOfficePopup :show="this.showOfficeDialog"-->
<!--                             @saveOffice="saveOffice"-->
<!--                             @closeOfficeDialog="this.showOfficeDialog = false">-->
<!--        </CreateOfficePopup>-->
<!--      </div>-->

<!--      <div class="service-block">-->
<!--        <div>-->
<!--          <h3>Типовые задачи</h3>-->
<!--          <SettingsListView :key="this.serviceListKey"-->
<!--                            :empty-header="'Список типовых задач пуст'"-->
<!--                            :elements-list="this.servicesList"-->
<!--                            :model-name="'service'"-->
<!--                            @deleteElement="loadServices">-->
<!--          </SettingsListView>-->
<!--        </div>-->

<!--        <MyButton @click="this.showServiceDialog = true">-->
<!--          Добавить типовую задачу-->
<!--        </MyButton>-->

<!--        <CreateServicePopup :show="this.showServiceDialog"-->
<!--                            @saveService="saveService"-->
<!--                            @closeServiceDialog="this.showServiceDialog = false">-->
<!--        </CreateServicePopup>-->
<!--      </div>-->
    </div>

    <div class="right-side">
<!--      <div class="schedule-block">-->
<!--        <div>-->
<!--          <h3>Графики работы</h3>-->

<!--          <SettingsListView :key="this.scheduleListKey"-->
<!--                            :empty-header="'Список графиков пуст'"-->
<!--                            :elements-list="this.schedulesList"-->
<!--                            :model-name="'schedule'"-->
<!--                            @deleteElement="loadSchedules">-->
<!--          </SettingsListView>-->
<!--        </div>-->

<!--        <MyButton @click="this.showScheduleDialog = true">-->
<!--          Добавить график работы-->
<!--        </MyButton>-->

<!--        <CreateWorkSchedulePopup :show="this.showScheduleDialog"-->
<!--                           @saveSchedule="saveSchedule"-->
<!--                           @closeScheduleDialog="this.showScheduleDialog = false">-->
<!--        </CreateWorkSchedulePopup>-->
<!--      </div>-->
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MyInput from "@/components/UI/MyInput.vue";
import MyButton from "@/components/UI/MyButton.vue";
import SettingsListView from "@/components/Settings/SettingsListView.vue";


export default {
  components: {
    SettingsListView,
    MyButton,
    MyInput
  },
  data() {
    return {
      // officesList: [],
      // officesListKey: 1,
      // showOfficeDialog: false,
      //
      // schedulesList: [],
      // scheduleListKey: 1,
      // showScheduleDialog: false,
      //
      // servicesList: [],
      // serviceListKey: 1,
      // showServiceDialog: false,
    }
  },
  created() {
    // this.loadOffices();
    // this.loadSchedules();
    // this.loadServices();
  },
  methods: {
    // async loadOffices() {
    //   const response = (await axios.get(`http://localhost:8000/api/v1/office/`))
    //   this.officesList = response.data
    // },
    // async createOffice(data) {
    //   try {
    //     await axios.post(
    //         'http://localhost:8000/api/v1/office/create/',
    //         {
    //           name: data.name,
    //           address: data.address,
    //           work_schedule: data.work_schedule
    //         }
    //     )
    //   } catch (e) {
    //     alert('Сервер не доступен')
    //   }
    //   this.reloadOffices()
    // },
    // saveOffice(data) {
    //   this.createOffice(data)
    //   this.showOfficeDialog = false
    // },
    // reloadOffices() {
    //   this.loadOffices();
    //   this.officesListKey = this.officesListKey + 1
    // },
    //
    // async loadSchedules() {
    //   const response = (await axios.get(`http://localhost:8000/api/v1/schedule/`))
    //   this.schedulesList = response.data
    // },
    // async createSchedule(data) {
    //   try {
    //     const response = (await axios.post(
    //         'http://localhost:8000/api/v1/schedule/create/',
    //         {
    //           name: data.scheduleName,
    //         }
    //     ))
    //     let newSchedulePk = response.data.id
    //     await this.configWorkDays(newSchedulePk, data.days)
    //   } catch (e) {
    //     alert('Сервер не доступен')
    //   }
    //   this.reloadSchedules()
    // },
    // async configWorkDays(newSchedulePk, days) {
    //   try {
    //     const response = (await axios.get(`http://localhost:8000/api/v1/schedule/${newSchedulePk}`))
    //     let workDays = response.data.work_days
    //
    //     for (let day in days) {
    //       await axios.put(
    //           `http://localhost:8000/api/v1/schedule/workday/manage/${workDays[days[day].dayId - 1].id}`,
    //           {
    //             is_not_working: false,
    //             start_time: days[day].start,
    //             end_time: days[day].end,
    //           }
    //       )
    //     }
    //   } catch (e) {
    //     alert('Сервер не доступен')
    //   }
    // },
    // saveSchedule(data) {
    //   this.createSchedule(data)
    //   this.showScheduleDialog = false
    // },
    // reloadSchedules() {
    //   this.loadSchedules();
    //   this.scheduleListKey = this.scheduleListKey + 1
    // },
    //
    // async loadServices() {
    //   const response = (await axios.get(`http://localhost:8000/api/v1/service/`))
    //   this.servicesList = response.data
    // },
    // async createService(data) {
    //   try {
    //     await axios.post(
    //         'http://localhost:8000/api/v1/service/create/',
    //         {
    //           name: data.name,
    //           description: data.description,
    //           position: data.position
    //         }
    //     )
    //   } catch (e) {
    //     alert('Сервер не доступен')
    //   }
    //   this.reloadServices()
    // },
    // saveService(data) {
    //   this.createService(data)
    //   this.showServiceDialog = false
    // },
    // reloadServices() {
    //   this.loadServices();
    //   this.servicesList = this.servicesList + 1
    // },
  },
}

</script>

<style scoped>
.inside-container {
  display: flex;
  flex-direction: row;
  height: 100%;
  width: 100%;
}

.left-side {
  width: 35%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin-right: 20px;
}

.right-side {
  width: 35%;
  display: flex;
  flex-direction: column;
}

.office-block {
  height: 45%;
  justify-content: space-between;
  display: flex;
  flex-direction: column;
}

.service-block {
  height: 45%;
  justify-content: space-between;
  display: flex;
  flex-direction: column;
}

.schedule-block {
  height: 45%;
  justify-content: space-between;
  display: flex;
  flex-direction: column;
}
</style>