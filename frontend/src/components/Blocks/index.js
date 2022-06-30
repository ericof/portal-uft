import userSVG from '@plone/volto/icons/user.svg';
import PersonBlockView from './PersonBlock/View';
import PersonBlockEdit from './PersonBlock/Edit';

const blocks = {
  personBlock: {
    id: 'personBlock',
    title: 'Person Block',
    icon: userSVG,
    group: 'midia',
    view: PersonBlockView,
    edit: PersonBlockEdit,
    restricted: false,
    mostUsed: true,
    sidebarTab: 1,
  },
};

export default blocks;
