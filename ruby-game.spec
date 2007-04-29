%define oname rubygame

Summary:	Rubygame is a cross-platform multimedia library for ruby
Name:		ruby-game
Version:	2.0.0
Release:	%mkrel 1
License:	LGPL
Group:		Development/Ruby
Url:		http://rubygame.sourceforge.net/
Source0:	http://downloads.sourceforge.net/rubygame/%{oname}-%{version}.tar.bz2
BuildRequires:	ruby-rake
BuildRequires:	SDL-devel
BuildRequires:	libSDL_gfx0-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
Requires:	ruby
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Rubygame is a cross-platform game-development extension 
and library for Ruby, inspired by Pygame.The purpose of 
Rubygame is to empower game developers by providing them 
with powerful and flexible high-level concepts. Instead 
of worrying about low-level technical details, you can 
focus your energy on more interesting things (like making a fun game).

Rubygames core is written in C to bind low-level SDL 
functions in ruby. On top of that is a pure ruby library 
for higher-level behavior like event and game object management.

%prep
%setup -qn %{oname}-%{version}

%build
rake build

rake rdoc

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
mkdir -p %{buildroot}{%{ruby_sitearchdir},%{ruby_sitelibdir}}

RUBYGAME_CONFIG="--sitearchdir %{buildroot}%{ruby_sitearchdir} --sitelibdir %{buildroot}%{ruby_sitelibdir}" rake install


%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc html/*
%attr(755,root,root) %{ruby_sitearchdir}/%{oname}*.so
%{ruby_sitelibdir}/*
