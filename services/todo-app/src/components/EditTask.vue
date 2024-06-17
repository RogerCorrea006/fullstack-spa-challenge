<template>
  <v-row class="mt-4">
    <v-col v-for="task in tasks" :key="task.id" sm="12" md="6" lg="4">
      <v-card>
        <v-form>
          <v-card-text>
            <v-row>
              <v-col>
                <v-text-field
                  label="Título"
                  counter
                  maxlength="20"
                  :value="task.name"
                  :disabled="!task.editable"
                  v-model="task.name"
                  :rules="rules"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-textarea
                  label="Descrição"
                  counter
                  maxlength="100"
                  :value="task.description"
                  :disabled="!task.editable"
                  v-model="task.description"
                  :rules="rules"
                >
                </v-textarea>
              </v-col>
            </v-row>
          </v-card-text>
          <v-card-actions>
            <v-btn
              v-if="task.editable"
              color="blue"
              @click="saveTask(task)"
              text
              >Salvar</v-btn
            >
            <v-btn
              v-if="!task.editable"
              color="blue"
              @click="editTask(task)"
              text
              >Editar</v-btn
            >
            <v-btn color="red" @click="deleteTask(task)" text>Excluir</v-btn>
          </v-card-actions>
        </v-form>
      </v-card>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import axios from "../plugins/axios";
import Vue from "vue";
import Component from "vue-class-component";
import { PropType } from "vue/types/v3-component-props";
import {Task} from "../interfaces/task"

const TasksPage = Vue.extend({
  props: {
    tasks: { type: [] as PropType<Task> },
  },
});

@Component
export default class EditTask extends TasksPage {
  rules = [
    (value: string) => !!value || "Campo obrigatório",
  ]
  
  
  editTask(task: Task) {
    task.editable = !task.editable;
  }

  async saveTask(task: Task) {

    if(task.name == "" || task.description == "") return

    try {
      const response = await axios.post(
        "/task/updateTask",
        {
          id: task.id,
          name: task.name,
          description: task.description,
        }
      );
      console.log(response.data)

      task.editable = !task.editable;
    } catch (error) {
      console.error("erro ao editar a tarefa:", error);
    }
  }

  async deleteTask(task: Task){

    try {
      const response = await axios.post(
        "/task/deleteTask",
        {
          id: task.id,
        }
      );
      console.log(response.data)

      this.$emit('taskDelete')

    } catch (error) {
      console.error("erro ao deletar a tarefa:", error);
    }
  }
}
</script>