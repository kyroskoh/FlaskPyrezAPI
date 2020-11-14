#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.http import (
  get_html,
  get_url,
)
def latest_video_func(channel_id):
  try:
    soup = get_html(f'http://www.youtube.com/channel/{channel_id}/videos').select_one('.yt-lockup-title a')
    _title, _url = soup['title'], soup['href']
    '''
    if soup and hasattr(soup, 'select_one'):
      soup = soup.select_one('.yt-lockup-title a')
      _title, _url = soup['title'], soup['href']
    '''
  except Exception:
    pass
  else:
    return f'{_title} - https://youtu.be/{_url.replace("/watch?v=", "")}'
  return get_url(f'https://api.crunchprank.net/youtube/latest_video?id={channel_id}', surpress_exception=False)