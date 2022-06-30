/**
 * Add your config changes here.
 * @module config
 * @example
 * export default function applyConfig(config) {
 *   config.settings = {
 *     ...config.settings,
 *     port: 4300,
 *     listBlockTypes: {
 *       ...config.settings.listBlockTypes,
 *       'my-list-item',
 *    }
 * }
 */

import CampusView from '@package/components/View/CampusView';
import PersonView from '@package/components/View/PersonView';
import blocks from '@package/components/Blocks';

// All your imports required for the config here BEFORE this line
import '@plone/volto/config';

export default function applyConfig(config) {
  config.settings = {
    ...config.settings,
    isMultilingual: false,
    supportedLanguages: ['pt-br'],
    defaultLanguage: 'pt-br',
  };
  config.views.contentTypesViews = {
    campus: CampusView,
    person: PersonView,
    ...config.views.contentTypesViews,
  };
  config.blocks.blocksConfig = {
    ...config.blocks.blocksConfig,
    ...blocks,
  };
  config.blocks.blocksConfig.__grid.gridAllowedBlocks = [
    ...config.blocks.blocksConfig.__grid.gridAllowedBlocks,
    'campusBlock',
    'personBlock',
  ];
  return config;
}
