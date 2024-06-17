<template>
  <v-container id="containerHome" class="my-5">
    <v-row v-if="tasks.length <= 0" class="mt-5" justify="center">
      <v-col class="text-center" sm=12>
        <h1 class="h1-no-tasks">
          Parece que você ainda não tem nenhuma tarefa
        </h1>
      </v-col>
      <v-col class="col-button" sm=12 >
        <v-btn large dark color="purple" router to="/tasks">
          Ir criar novas Tarefas
        </v-btn>
      </v-col>
    </v-row>
    <card-task :tasks="tasks" v-on:getTasks="getTasks" />
  </v-container>
</template>


<style>
.col-button{
  display: flex;
  justify-content: center;
}
</style>


<script lang="ts">


import axios from "../plugins/axios";
import Vue from "vue";
import Component from "vue-class-component";
import CardTask from "./CardTask.vue";
import {Task} from "../interfaces/task"

@Component({
  components: {
    CardTask
  }
})
export default class HomePage extends Vue {

  tasks: Task[] = []

  mounted(){
    this.getTasks()
  }

  async getTasks() {

    try {

      const response = await axios.get<Task[]>('/task/getTasks')
      this.tasks = response.data

    } catch (error){
      console.error('erro ao buscar as tarefas:', error)
    }

    
  }


}
</script>