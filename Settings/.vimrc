" VIM configuration file
" Description: OPtimized for C/C++ development
" Author: Gerhard Gappmeier
" Edited by: Marshall Farrier
" http://gergap.wordpress.com/2009/05/29/minimal-vimrc-for-cc-developers/
"
" set UTF-8 encoding
set enc=utf-8
set fenc=utf-8
set termencoding=utf-8
" disable vi compatibility
set nocompatible
"filetype plugin indent on
" use indentation of previous line
set autoindent
" use intelligent indentation for C (smartindent causes problems with Python comments)
" set smartindent
filetype indent on
set tabstop=4
set shiftwidth=4
"expand tabs to spaces
set expandtab
" wrap lines at 120 chars
" set textwidth=120
" wrap but don't break long lines
set wrap
set linebreak
set textwidth=0
set wrapmargin=0
" turn syntax highlighting on
set t_Co=256
syntax on
" turn line numbers on
set number
" highlight matching braces
set showmatch
" intelligent comments
set comments=sl:/*,mb:\ *,elx:\ */
set formatoptions+=r
set formatoptions+=c
set formatoptions+=o
" Show context around current line
set scrolloff=16
