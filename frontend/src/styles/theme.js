import { defaultTheme } from 'evergreen-ui';
import { merge } from 'lodash';

const myCustomTheme = merge({}, defaultTheme, {
  typography: {
    fontFamilies: {
      display: '-apple-system, poppins',
      ui: '-apple-system, sans-serif',
      mono: '"SF Mono", monospace'
    }
  }
})

export default myCustomTheme;