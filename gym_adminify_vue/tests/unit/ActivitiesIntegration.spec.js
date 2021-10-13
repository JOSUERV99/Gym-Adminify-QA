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

describe('Activities.vue integration test', () => {

  let wrapper, dummyActivities, dummyActivitiesData;

  beforeAll(() => {

    // Component with default values
    dummyActivitiesData = {
      activityStartTime_new: '10:30',
      activityEndTime_new: '10:30',
      activityDay_edit : 1,
      days: '',
      activityDay_edit: '',
      changing: '',
      activities : []
    }

    // dummy activities for axios.put calls
    dummyActivities = [
      {
          id: 4,
          client: [],
          dayofmonth: 1,
          teacher: {
              name: "Miguel",
              get_absolute_url: "/1/"
          },
          unrolled_clients: [
              {
                  name: "enrtique",
                  person: 3
              }
          ]
      }
    ]

    // mount the activities vue component with dummy data
    wrapper = shallowMount(Activities, {
      data() {
        return dummyActivitiesData
      },
      global: {
        mocks: {
          $store: store,
        }
      }
    })
  })

  beforeEach(() => {
    mockAxios.put.mockImplementationOnce(() =>
    Promise.resolve({
      status : 202
    }));
  })

  afterEach(() => {
    mockAxios.reset();
  });

  it('Escenario donde la actividad tenga clientes matriculados', () => {
    
    // let's try to save the modified activity
    wrapper.vm.saveModifyActivity(dummyActivities).then(() => {
      expect(mockAxios.put).toHaveBeenCalledTimes(0);
    })
  })

  it('Escenario donde la actividad no tenga clientes matriculados', () => {

    // let's try to save the modified activity 
    wrapper.vm.saveModifyActivity([]).then(() => {
      expect(mockAxios.put).toHaveBeenCalledTimes(1);
    });
  });

  it('Escenario donde la lista de clientes matriculados sea nula', () => {

    // let's try to save the modified activity
    wrapper.vm.saveModifyActivity(null).then(() => {
      expect(mockAxios.put).toHaveBeenCalledTimes(0);
    })
  });
})