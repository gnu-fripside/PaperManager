<template>
    <div class="fileInfo">
    <el-form :model="Paper" :rules="rules" ref="Paper" label-width="100px" class="paperInfo">
      <el-form-item label="Class" prop="class">
        <el-cascader
          :options="classTree"
          v-model="classes"
          @change="changeClass">
        </el-cascader>
      </el-form-item>
      <el-form-item label="Title" prop="title">
        <el-input
          :placeholder="Paper.title"
          v-model="Paper.title">
        </el-input>
      </el-form-item>
      Author:
      <el-row v-for="author in Paper.authors">>
        <el-col :span="6">
          <el-form-item
            label="first name"
            :prop="'first_name_' + author.first_name + '_' + author.last_name"
            >
            <el-input
              :placeholder="author.first_name"
              v-model="author.first_name">
            </el-input>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item
            label="last name"
            :prop="'last_name_' + author.first_name + '_' + author.last_name">
            <el-input
              :placeholder="author.last_name"
              v-model="author.last_name">
            </el-input>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item
            label="email"
            :prop="'email_' + author.first_name + '_' + author.last_name">
            <el-input
              :placeholder="author.email"
              v-model="author.email">
            </el-input>
          </el-form-item>
        </el-col>
        <el-button
          @click="deleteAuthor(author)">
          Delete
        </el-button>
      </el-row>
      <el-button
        @click="addAuthor">
        Add Author
      </el-button>
      <el-form-item
        label="Publish Time"
        prop="Publish Time">
        <el-date-picker
          type="date"
          :placeholder="Paper.publish_time"
          v-model="Paper.publish_time">
        </el-date-picker>
      </el-form-item>
      <el-form-item
        label="Source"
        prop="source">
        <el-input
          :placeholder="Paper.source"
          v-model="Paper.source">
        </el-input>
      </el-form-item>
      <el-form-item
        label="URL"
        prop="url">
        <el-input
          :placeholder="Paper.url"
          v-model="Paper.url">
        </el-input>
      </el-form-item>
    </el-form>
    <el-button
      type="primary"
      @click="submitForm('Paper')">
      Submit Changes
    </el-button>
  </div>
</template>

<script>
    export default {
        name: 'fileInfo',
        data () {
            return {
                Paper: {
                    username: "",
                    title: "",
                    authors: [
                        {
                            first_name: "aa",
                            last_name: "b",
                            email: "c",
                        },
                        {
                            first_name: "alah",
                            last_name: "uhak",
                            email: "bah",
                        },
                    ],
                    publish_time: "",
                    add_time: "",
                    source: "",
                    url: "",
                    hash_code: "",
                    classification_tree_node: "",
                    log: ""
                },
                classTree: [
                    {
                        value: 'cs',
                        label: 'cs',
                        children: [
                            {
                                value: 'ai',
                                label: 'ai',
                                children: [
                                    {
                                        value: 'cv',
                                        label: 'cv'
                                    },
                                    {
                                        value: 'nlp',
                                        label: 'nlp'
                                    }
                                ]
                            },
                            {
                                value: 'system',
                                label: 'system',
                                children: [
                                    {
                                        value: 'os',
                                        label: 'os'
                                    },
                                    {
                                        value: 'hardware',
                                        label: 'hardware'
                                    }
                                ]
                            }
                        ]
                    }
                ],
                classes: []
            };
        }
    }
</script>
