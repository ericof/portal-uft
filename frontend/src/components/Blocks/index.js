import homeSVG from '@plone/volto/icons/home.svg';
import userSVG from '@plone/volto/icons/user.svg';
import CampusBlockView from './CampusBlock/View';
import CampusBlockEdit from './CampusBlock/Edit';
import PersonBlockView from './PersonBlock/View';
import PersonBlockEdit from './PersonBlock/Edit';

const blocks = {
  campusBlock: {
    id: 'campusBlock',
    title: 'Campus Block',
    icon: homeSVG,
    group: 'media',
    view: CampusBlockView,
    edit: CampusBlockEdit,
    restricted: false,
    mostUsed: false,
    sidebarTab: 1,
  },
  personBlock: {
    id: 'personBlock',
    title: 'Person Block',
    icon: userSVG,
    group: 'media',
    view: PersonBlockView,
    edit: PersonBlockEdit,
    restricted: false,
    mostUsed: true,
    sidebarTab: 1,
  },
};

export default blocks;
