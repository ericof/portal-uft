import homeSVG from '@plone/volto/icons/home.svg';
import twitterSVG from '@package/icons/twitter.svg';
import userSVG from '@plone/volto/icons/user.svg';
import CampusBlockView from './CampusBlock/View';
import CampusBlockEdit from './CampusBlock/Edit';
import PersonBlockView from './PersonBlock/View';
import PersonBlockEdit from './PersonBlock/Edit';
import TwitterBlockView from './Twitter/View';
import TwitterBlockEdit from './Twitter/Edit';

const blocks = {
  campusBlock: {
    id: 'campusBlock',
    title: 'Campus Block',
    icon: homeSVG,
    group: 'uft',
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
    group: 'uft',
    view: PersonBlockView,
    edit: PersonBlockEdit,
    restricted: false,
    mostUsed: true,
    sidebarTab: 1,
  },
  twitterBlock: {
    id: 'twitterBlock',
    title: 'Twitter',
    icon: twitterSVG,
    group: 'media',
    view: TwitterBlockView,
    edit: TwitterBlockEdit,
    restricted: false,
    mostUsed: true,
    sidebarTab: 1,
  },
};

export default blocks;
