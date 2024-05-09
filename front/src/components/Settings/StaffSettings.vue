<template>
  <div class="inside-container">
    <div class="outer-block">
      <div class="inner-block">
        <div>
          <h3>Отделы</h3>

          <SettingsListView :key="this.departmentsListKey"
                            :empty-header="'Список отделов пуст'"
                            :elements-list="this.departmentsList"
                            :model-name="'department'"
                            @deleteElement="loadDepartments">
          </SettingsListView>
        </div>

        <MyButton @click="this.showDepartmentDialog = true">
          Добавить отдел
        </MyButton>

        <CreateDepartmentPopup :show="this.showDepartmentDialog"
                               @saveDepartment="saveDepartment"
                               @closeDepartmentDialog="this.showDepartmentDialog = false">
        </CreateDepartmentPopup>
      </div>

      <div class="inner-block">
        <div>
          <h3>Должности</h3>

          <SettingsListView :key="this.positionsListKey"
                            :empty-header="'Список должностей пуст'"
                            :elements-list="this.positionsList"
                            :model-name="'position'"
                            @deleteElement="loadPositions">
          </SettingsListView>
        </div>

        <MyButton @click="this.showPositionDialog = true">
          Добавить должность
        </MyButton>

        <CreatePositionPopup :show="this.showPositionDialog"
                             @save="savePosition"
                             @closeDialog="this.showPositionDialog = false">
        </CreatePositionPopup>
      </div>
    </div>

    <div class="outer-block">
      <div class="inner-block">
        <div>
          <h3>Сотрудники</h3>

          <SettingsListView :key="this.employeesListKey"
                            :empty-header="'Список сотрудников пуст'"
                            :elements-list="this.employeesList"
                            :model-name="'employee'"
                            @deleteElement="loadEmployees">
          </SettingsListView>
        </div>

        <MyButton @click="this.showEmployeeDialog = true">
          Добавить сотрудника
        </MyButton>

        <CreateEmployeePopup :show="this.showEmployeeDialog"
                             @save="saveEmployee"
                             @closeDialog="this.showEmployeeDialog = false">
        </CreateEmployeePopup>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MyInput from "@/components/UI/MyInput.vue";
import MyButton from "@/components/UI/MyButton.vue";
import SettingsListView from "@/components/Settings/SettingsListView.vue";
import CreateDepartmentPopup from "@/components/Settings/CreateDepartmentPopup.vue";
import CreatePositionPopup from "@/components/Settings/CreatePositionPopup.vue";
import CreateEmployeePopup from "@/components/Settings/CreateEmployeePopup.vue";


export default {
  components: {
    CreateEmployeePopup,
    CreatePositionPopup,
    CreateDepartmentPopup,
    SettingsListView,
    MyButton,
    MyInput
  },
  data() {
    return {
      departmentsList: [],
      departmentsListKey: 1,
      showDepartmentDialog: false,

      positionsList: [],
      positionsListKey: 1,
      showPositionDialog: false,

      employeesList: [],
      employeesListKey: 1,
      showEmployeeDialog: false,
    }
  },
  created() {
    this.loadDepartments();
    this.loadPositions();
    this.loadEmployees();
  },
  methods: {
    async loadDepartments() {
      const response = (await axios.get(`http://localhost:8000/api/v1/department/`))
      this.departmentsList = response.data
    },
    async createDepartment(data) {
      try {
        await axios.post(
            'http://localhost:8000/api/v1/department/create/',
            {
              name: data.name,
            }
        )
      } catch (e) {
        alert('Сервер не доступен')
      }
      this.reloadDepartments()
    },
    saveDepartment(data) {
      this.createDepartment(data)
      this.showDepartmentDialog = false
    },
    reloadDepartments() {
      this.loadDepartments();
      this.departmentsListKey += 1
    },

    async loadPositions() {
      const response = (await axios.get(`http://localhost:8000/api/v1/position/`))
      this.positionsList = response.data
    },
    async createPosition(data) {
      try {
        await axios.post(
            'http://localhost:8000/api/v1/position/create/',
            {
              name: data.name,
              department: data.department
            }
        )
      } catch (e) {
        alert('Сервер не доступен')
      }
      this.reloadPositions()
    },
    savePosition(data) {
      this.createPosition(data)
      this.showPositionDialog = false
    },
    reloadPositions() {
      this.loadPositions();
      this.positionsListKey += 1
    },

    async loadEmployees() {
      const response = (await axios.get(`http://localhost:8000/api/v1/employee/`))
      this.employeesList = response.data
    },
    async createEmployee(data) {
      try {
        await axios.post(
            'http://localhost:8000/api/v1/employee/create/',
            {
              surname: data.surname,
              name: data.name,
              patronymic: data.patronymic,
              phone: data.phone,
              email: data.email,
              office: data.selectedOffice,
              position: data.selectedPosition,
              tg_id: data.tgId,
            }
        )
      } catch (e) {
        alert('Сервер не доступен')
        console.log(e)
      }
      this.reloadEmployees()
    },
    saveEmployee(data) {
      this.createEmployee(data)
      this.showEmployeeDialog = false
    },
    reloadEmployees() {
      this.loadEmployees();
      this.employeesListKey += 1
    },
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

.outer-block {
  width: 35%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin-right: 20px;
}

.inner-block {
  height: 45%;
  justify-content: space-between;
  display: flex;
  flex-direction: column;
}
</style>