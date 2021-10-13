import { shallowMount, createLocalVue } from '@vue/test-utils'
import Activities from '../../src/views/Activities.vue'
import Vuex from 'vuex'

const store = new Vuex.Store({
                              state: {
                                permissions: []
                              },
                              mutations: {
                                setIsLoading(state,status){
                                  state.isLoading = status
                                }
                              },
                            })


describe('Activities.vue', () => {
  it('renders a message and responds correctly to user input', () => {
    const wrapper = shallowMount(Activities, {
      data() {
        return {
          activityStartTime_new: '10:30',
          activityEndTime_new: '10:30',
          activityCapacity_edit: '10',
          activityDay_edit: 'Lunes',
          days: ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo'],
          activityStartTime_edit: '10:30',
          activityEndTime_edit: '11:30'
        }
      },
      global: {
      mocks: {
        $store: store,
      }
    } })

    expect(wrapper.vm.validateHours()).toBe(true);
    expect(wrapper.vm.saveModifyActivity(0)).toMatchObject({});

  })
})
