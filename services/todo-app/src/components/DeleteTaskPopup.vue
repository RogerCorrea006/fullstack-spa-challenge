<template>
  
   
      <v-card>
        <v-card-title>
          <span class="text-h5">Excluir Tarefa</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col>
                Deseja realmente excluir a tarefa "{{editTask.name}}" ?
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="$emit('closeDialog')">
            Fechar
          </v-btn>
          <v-btn color="red" text @click="deleteTask"> Excluir </v-btn>
        </v-card-actions>
      </v-card>
   

</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import axios from "../plugins/axios";
import { PropType } from "vue/types/v3-component-props";
import {Task} from "../interfaces/task"


const CardTask = Vue.extend({
  props: {
    editTask: { type: Object as PropType<Task> },
  },
});

@Component
export default class DeleteTaskPopup extends CardTask {

  data() {
    return {};
  }

  async deleteTask() {
    try {
      await axios.post(
        "/task/deleteTask",
        {
          id: this.editTask.id,
        }
      );

      this.$emit('tasksUpdated')
      this.$emit('closeDialog')

    } catch (error) {
      console.error("erro ao excluir a tarefa:", error);
    }
  }

}
</script>