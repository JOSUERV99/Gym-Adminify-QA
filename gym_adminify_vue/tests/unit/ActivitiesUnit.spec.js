import { shallowMount, createLocalVue } from '@vue/test-utils'
import Activities from '../../src/views/Activities.vue'
import Vuex from 'vuex';
import mockAxios from 'jest-mock-axios';

process.on('unhandledRejection', () => {});
jest.mock('axios');

const store = new Vuex.Store({
    state: {
        permissions: []
    },
    mutations: {
        setIsLoading(state,status) {
            state.isLoading = status
        }
    },
});

describe('Activities.vue Unit test', () => {

  let wrapper;

  beforeAll(() => {
    // Component with default values
    wrapper = shallowMount(Activities, {
      data() {
        return {
          activityCapacity_edit: '',
          days: '',
          activityDay_edit: '',
          activityStartTime_edit: '',
          activityEndTime_edit: '',
          changing: ''
        }
      },
      global: {
        mocks: {
          $store: store,
        }
      }
    })
  });


  afterEach(() => {
    mockAxios.reset();
  });

  /*
  * 1	Escenario donde el id de la actividad a modificar no exista
  * 2	Escenario donde el id de la actividad a modificar sea negativo
  * 5 Escenario con capacidad en el request body negativo
  */
  it('Escenario donde el id de la actividad a modificar no exista', async () => {
    
    wrapper.setData({
      capacity: '10',
      dayofweek: '1',
      startime: '10:30',
      endtime: '11:30',
      changing: 10
    })

    // let's try to save the modified activity
    await expect(wrapper.vm.saveModifyActivity([]))
    .rejects
    .not
    .toThrow("Cannot read property 'then' of undefined");
  });

  it('Escenario donde el id de la actividad a modificar sea negativo', async () => {
    
    wrapper.setData({
      capacity: '10',
      dayofweek: '1',
      startime: '10:30',
      endtime: '11:30',
      changing: '-10'
    })

    // let's try to save the modified activity
    await expect(wrapper.vm.saveModifyActivity([]))
    .rejects
    .not
    .toThrow("Cannot read property 'then' of undefined");
  });

  it('Escenario con capacidad en el request body negativo', async () => {
    
    wrapper.setData({
      capacity: '-10',
      dayofweek: '1',
      startime: '10:30',
      endtime: '11:30',
      changing: '10'
    })
    
    // let's try to save the modified activity
    await expect(wrapper.vm.saveModifyActivity([]))
    .rejects
    .not
    .toThrow("Cannot read property 'then' of undefined");
  })
});