<template>
  <div class="showPdf">
        <el-row :gutter="10">
            <el-radio v-model="radio" label="0">Unread</el-radio>
            <el-radio v-model="radio" label="1">Roughly</el-radio>
            <el-radio v-model="radio" label="2">Clearly</el-radio>
        </el-row>

        <input type="checkbox" v-model="show">
        <select v-model="src" style="width: 10em">
          <option v-for="item in pdfList" :value="item" v-text="item"></option>
        </select>
        <input v-model.number="page" type="number" style="width: 5em"> /{{numPages}}
        <el-button @click="rotate += 90">&#x27F3;</el-button>
        <el-button @click="rotate -= 90">&#x27F2;</el-button>
        <el-button @click="$refs.pdf.print()">print</el-button>
        <el-button @click="exportFile">export</el-button>

        <div>
          <el-row :gutter="20">
            <el-col :span="17">
              <div v-if="loadedRatio > 0 && loadedRatio < 1" style="background-color: green; color: white; text-align: center" :style="{ width: loadedRatio * 100 + '%' }">{{ Math.floor(loadedRatio * 100) }}%</div>
              <pdf v-if="show" ref="pdf" style="border: 1.8px liquid red" :src="src" :page="page" :rotate="rotate" @password="password" @progress="loadedRatio = $event" @error="error" @numPages="numPages = $event"></pdf>
            </el-col>
            <el-col :span="7">
              <el-tabs type="border-card">
                <el-tab-pane label="Editer">
                  <textarea :value="input" @input="update" cols="44" rows="40"></textarea>
                  <br>
                  <el-button :value="submit" @click="submitNote">Submit note</el-button>
                </el-tab-pane>
                <el-tab-pane label="View">
                  <div v-html="compiledMarkdown"></div>
                </el-tab-pane>
              </el-tabs>
            </el-col>
          </el-row>
        </div>
  </div>
</template>
<script>

import pdf from 'vue-pdf'

export default {
    name: "showPdf",
    components: {
        pdf: pdf
    },
    data () {
        return {

            show: true,
            pdfList: [
                '',
                'https://cdn.mozilla.net/pdfjs/tracemonkey.pdf',
                'https://arxiv.org/pdf/1604.02135.pdf',
                'https://arxiv.org/pdf/1504.08083.pdf',
            ],
            radio: "0",
            src:'',
            loadedRatio: 0,
            page: 1,
            numPages: 0,
            rotate: 0,
            input: "# hello"
        }
    },
    computed: {
        compiledMarkdown: function () {
            var marked = require('marked');
            return marked(this.input, { sanitize: true});
        }
    },
    methods: {
        password: function(updatePassword, reason) {
            updatePassword(prompt('password is "test"'));
        },
        error: function(err) {
            console.log(err);
        },
        update: function (e) {
            this.input = e.target.value
        },
        exportFile: {}
    }
}
</script>

